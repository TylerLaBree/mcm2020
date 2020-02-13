import matplotlib.pyplot as plt
import numpy as np
import printer

print("Hewwo World.")
print("mcm2020!!!")
print("big yeet")
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
#plt.show()
printer.pdf_print("output/test.pdf", x, np.cos(x))
