x = 0 #I imagine x being an on off switch/signal
def valve(x):
    if x == 0:
        return 'Valve open.'
    if x != 0:
        return 'Valve closed.'
pressure = int(input("Pressure Start: "))
while pressure < 3:
    print(f"{pressure}psi, everything's okay: {valve(x)}")
    pressure = pressure + 1
    if pressure == 3 or pressure > 3:
        break
x = 1
print(f"{pressure}psi, Danger! pressure too high. automatic shutdown initiated!: {valve(x)}")

#1psi, everything's okay: Valve open.
#2psi, everything's okay: Valve open.
#3psi, Danger! pressure too high. automatic shutdown initiated!: Valve closed.

