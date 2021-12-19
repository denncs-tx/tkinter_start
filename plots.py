from denncs import DennCSApp, ttk
import numpy as np
import matplotlib.pyplot as plt


class MyApp(DennCSApp):
    def __init__(self):
        super().__init__()
        ttk.Button(self, text="Graph It!", command=self._graph).pack()

    @staticmethod
    def _graph():
        house_prices = np.random.normal(20000, 25000, 5000)
        plt.polar(house_prices)
        plt.show()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
