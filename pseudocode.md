pseudocode for RPG Game
Jason Zhao
February 27th 2020

Menu code:
    input company name
    game start
        import time
    game stop

Pre-game code:

output "you are CEO of 'company name', a small business that you plan on growing to become the wealthiest company in the world"
output "your job is to manage your company and employees to maximize profits"


Money counter code:
    def increase_value_evrey_t_sec(initail_value, interval,/ increase_by,stop_after = -1):/
counter = 0/
values = []/
    while counter < stop_after or stop_after == -1:/
        time.sleep(interval)/
        initail_value += increase_by/
        print(initail_value)/
        values.append(initail_value)/
        counter += 1/
        increases over time at a constant rate until changed by player inputs/

    if profits = 70 000
    and time < 70 s
        print(evade taxes)
        remove taxes from Profits
        increase Profits
        taxesdefault = -0.2*(profits)

Player code:/
while time>0/
output: What will you do,/
    if player inputs:/
    1: Hire employee/
    2: Fire employee/
    3: Manage Profits/
    W: move north/
    A: move west/
    S: move south/
    D: Move east/

Map Code:
2x2 Map
print image of map and where player is

Employee code:
    hire employee "add to a list"
        subtracts profit
        increases rate of counter
    fire employee "removes from list"
        increases profit
        decreases rate of counter

status code:
if player input (I)
    print(value of profit)
    print(rate of profit)
    print(efficiency)
    print(number of employees)
    print(list of employees)

Invalid Input Code:
    print(invalid input)

stop code:
    player input END
        game stops
    if profit = 1 000 000
        game stops
