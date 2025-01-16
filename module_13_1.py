import asyncio

async def start_strongman(name, power):
    k = 7    # 7 - так как минимальное число, не кратное ни одному из аргументов "power"
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(k/power)
        print(f'Силач {name} поднял {i}-й шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Паша', 3))
    task_2 = asyncio.create_task(start_strongman('Денис', 4))
    task_3 = asyncio.create_task(start_strongman('Артур', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())