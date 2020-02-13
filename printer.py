import matplotlib.pyplot as plt


def pdf_print(fname, x, y):
    plt.plot(x, y)
    plt.savefig(fname)
    print("hello printer")
