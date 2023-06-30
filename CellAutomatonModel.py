import numpy as np


class CellAutomatonModel:
    def __init__(self, Rule, Boundary="Periodic"):
        self.Rule = Rule
        self.Rule_list = np.array(
            [int(i) for i in list(bin(Rule)[2:].zfill(8))]
        )
        self.Boundary = Boundary

    def Periodic(self, Cells):
        # Cells is only numpy array
        New_Cells = self.Rule_list[
            7
            - (
                np.roll(Cells, 1) * 2**2
                + Cells * 2**1
                + np.roll(Cells, -1) * 2**0
            )
        ]
        return New_Cells

    def Fix(self, Cells, Params):
        # Cells is only numpy array
        Cells = np.insert(Cells, [0, -1], Params)
        New_Cells = self.Rule_list[
            7
            - (
                np.roll(Cells, 1) * 2**2
                + Cells * 2**1
                + np.roll(Cells, -1) * 2**0
            )
        ]
        return New_Cells[1:-1]

    def kaihou(
        self,
    ):
        # Cells is only numpy array
        pass

    def Calculation(self, Cells, Params):
        if self.Boundary == "Periodic":
            return self.Periodic(Cells)
        elif self.Boundary == "Fix":
            return self.Fix(Cells, Params[0])

    def CA(self, X, Step, *args):
        Params = args
        Cells = np.empty((Step, len(X)), dtype=np.int8)
        Cells[0] = X
        for s in range(1, Step):
            Cells[s] = self.Calculation(Cells[s - 1], Params)

        return Cells

    def print(self, Cells):
        for c in Cells:
            for i in c:
                print(i, end="")
            print()

    def plot(self, Cells, DIR=""):
        import matplotlib.pyplot as plt

        plt.figure()
        plt.title(f"Rule{self.Rule}_Spatio")
        plt.imshow(Cells, cmap="binary", vmin=0, vmax=1, aspect="equal")
        # plt.axis("off")
        plt.tick_params(
            labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False,
            bottom=False,
            left=False,
            right=False,
            top=False,
        )
        plt.xlabel("Space")
        plt.ylabel("Time")
        plt.savefig(DIR + f"Rule{self.Rule}_Spatio.png", dpi=300)
        plt.show()


if __name__ == "__main__":
    Rule = 90
    L = 101

    # X       = np.random.choice([0,1], size=L)
    X = np.zeros(L)
    X[int(L / 2)] = 1

    # CA = CellAutomatonModel(Rule, Boundary="Fix")
    CA = CellAutomatonModel(Rule, Boundary="Periodic")
    Cells = CA.CA(X, 101)
    CA.print(Cells)
    CA.plot(Cells, DIR="01_Simulation/Output/")
