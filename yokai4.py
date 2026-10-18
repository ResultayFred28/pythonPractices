def detechGraphics(ram_gb,gpu_utilization):

    if ram_gb >= 8 and gpu_utilization <= 70:
        return "Ultra"
    elif ram_gb >= 4 and gpu_utilization <= 85:
        return "HD"
    else:
        return "Smooth"



ram = int(input("enter your pc ramGB: "))
gpu = int(input("enter your gpu utilization: "))

result = detechGraphics(ram,gpu)

print(result)