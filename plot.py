#  simulator-2022-nca - Simpy simulator of online scheduling between edge nodes
#  Copyright (c) 2021 - 2022. Gabriele Proietti Mattia <pm.gabriele@outlook.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os

import matplotlib.pyplot as plt

PLOT_DIRECTORY = "_plot"

markers = [r"$\triangle$", r"$\square$", r"$\diamondsuit$", r"$\otimes$", r"$\star$"]


class PlotUtils:
    """Plot utilities"""

    @staticmethod
    def use_tex():
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['text.usetex'] = True
        plt.rcParams['text.latex.preamble'] = r'''
            \DeclareUnicodeCharacter{03BB}{$\lambda$}
            \DeclareUnicodeCharacter{03BC}{$\mu$}
            \usepackage[utf8]{inputenc}
            \usepackage{amssymb}
            \usepackage{mathptmx}
            \usepackage[T1]{fontenc}
            '''
        # \usepackage[libertine]{newtxmath}
        # \usepackage[libertine]{newtxmath}\usepackage[T1]{fontenc}
        return True


class Plot:
    @staticmethod
    def plot(x_arr, y_arr, x_label, y_label, filename=None, fullpath=None, title=None, marker=None):
        plt.clf()
        fig, ax = plt.subplots()
        line_experimental, = ax.plot(x_arr, y_arr, marker=marker, markersize=3.0, markeredgewidth=1, linewidth=0.7)

        if title is not None:
            ax.set_title(title)

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        fig.tight_layout()
        os.makedirs(PLOT_DIRECTORY, exist_ok=True)

        if fullpath is not None:
            plt.savefig(fullpath)
        else:
            plt.savefig("{}/{}.pdf".format(PLOT_DIRECTORY, filename))

        plt.close(fig)

    @staticmethod
    def multi_plot(x_arr_arr, y_arr_arr, x_label, y_label, filename='plot', legend=None, title=None, log=False, xlim=None,
                   ylim=None, legend_position=None, show_markers=True, linewidth=0.6, fullpath=None, figw=6.4, figh=4.8):
        if len(x_arr_arr) != len(y_arr_arr):
            print("Size mismatch")
            return

        plt.clf()
        fig, ax = plt.subplots()
        legend_arr = []

        for i in range(len(y_arr_arr)):
            line, = ax.plot(x_arr_arr[i], y_arr_arr[i], markerfacecolor='None', linewidth=linewidth,
                            marker=markers[i % len(markers)] if show_markers else "",
                            markersize=5, markeredgewidth=0.6)
            if log:
                ax.set_yscale('log')
            if xlim is not None:
                ax.set_xlim(xlim)
            if ylim is not None:
                ax.set_ylim(ylim)
            if legend is not None:
                legend_arr.append(line)

        if legend_position is not None:
            plt.rcParams["legend.loc"] = str(legend_position)

        if legend is not None and len(legend) == len(legend_arr):
            plt.legend(legend_arr, legend, fontsize="small") # , loc="lower right")

        if title is not None:
            ax.set_title(title)

        # ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        fig.tight_layout()
        os.makedirs(PLOT_DIRECTORY, exist_ok=True)

        fig.set_figwidth(figw)  # 6.4
        fig.set_figheight(figh)  # 4.8

        if fullpath is not None:
            plt.savefig(fullpath)
        else:
            plt.savefig("{}/{}.pdf".format(PLOT_DIRECTORY, filename))

        plt.close(fig)

    @staticmethod
    def plot_bar_chart(x_arr, y_arr, x_label, y_label, filename=None, fullpath=None, title=None):
        plt.clf()
        fig, ax = plt.subplots()

        ax.bar(x_arr, y_arr)

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

        if fullpath is not None:
            plt.savefig(fullpath)
        else:
            plt.savefig("{}/{}.pdf".format(PLOT_DIRECTORY, filename))

        plt.close(fig)

    @staticmethod
    def plot_heatmap(mat, x_ticks, y_ticks, filename=None, fullpath=None, title=None, cbarlabel=None, y_label=None, x_label=None, vertical_xlabels=False):
        plt.clf()
        fig, ax = plt.subplots()

        im = ax.imshow(mat, cmap="YlGn")
        if cbarlabel is not None:
            cbar = ax.figure.colorbar(im, ax=ax)
            cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        ax.set_xticks(list(range(len(x_ticks))))
        ax.set_yticks(list(range(len(y_ticks))))
        ax.set_xticklabels(x_ticks, rotation="vertical" if vertical_xlabels else None)
        ax.set_yticklabels(y_ticks)
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)

        fig.tight_layout()

        if fullpath is not None:
            plt.savefig(fullpath)
        else:
            plt.savefig("{}/{}.pdf".format(PLOT_DIRECTORY, filename))

        plt.close(fig)
