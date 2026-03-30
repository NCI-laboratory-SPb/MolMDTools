import matplotlib.pyplot as plt
import numpy as np

class NCIL_Graph:
    """Class NCIL_Graph.
    
    """

    def __init__(self, title="NCIL graph", figsize=(10, 6)):
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.title = title

        self.colors = [
            "#2e7d32",  # зелёный
            "#66bb6a",  # светло-зелёный
            "#a5d6a7",  # совсем светло-зелёный
            "#1b5e20",  # тёмно-зелёный
        ]

        self.lines = []

    def add_line(self, x, y, label=None, linestyle='-', linewidth=2):
        color = self.colors[len(self.lines) % len(self.colors)]
        line, = self.ax.plot(x, y, linestyle=linestyle,
                             linewidth=linewidth,
                             color=color,
                             label=label)
        self.lines.append(line)

    def set_labels(self, xlabel="", ylabel=""):
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)

    def set_title(self, title):
        self.ax.set_title(title)

    def enable_grid(self):
        self.ax.grid(True, linestyle="--", alpha=0.5)

    def show_legend(self):
        self.ax.legend()

    def show(self):
        self.ax.set_title(self.title)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plt_clv_clv(clvs_lsts, colvar1_num=0, colvar2_num=1, title='Graph', x_label='q1', y_label='q1', font_size=14, trandline=False):
        """Get lists of coolvars and make plot colvar_1 - colvar_2"""
        x = clvs_lsts.colvars_lsts[colvar1_num]
        y = clvs_lsts.colvars_lsts[colvar2_num]

        if len(clvs_lsts.colvars_lsts) < 2:
            print("We can't make plot for one collective variable.")
            return None
        
        plt.title(title, fontsize=int(font_size))
        plt.xlabel(x_label+'_'+str(colvar1_num), fontsize=int(font_size))
        plt.ylabel(y_label+'_'+str(colvar2_num), fontsize=int(font_size))
        plt.scatter(x, y, s = 1)

        if trandline == 'linear':
            a, b = np.polyfit(x, y, 1)
            y_trend = a*x + b
            equation = f'y = {round(a, 2)}x + {round(b, 2)}'
            plt.text(0.5, 0.9, equation, fontsize=font_size, transform=plt.gca().transAxes)
            plt.plot(x, y_trend, color = 'red')

        plt.show()
        return None