def calculate_std_dev(nums: list[float]) -> float:
    somma=0
    media=0
    varianza=0
    if len(nums)==0:
        raise ValueError("lista vuota")
    else:
        for num in nums:
            somma+=num
        media=somma/len(nums)

        for numeo in nums:
            diff=numeo-media
            varianza+= diff*diff
        varianza=varianza/len(nums)
        radice =varianza
        for _ in range(10):
            radice=0.5*(radice+varianza/radice)
        return radice


print(calculate_std_dev([1.0, 2.0, 3.0, 4.0, 5.0]))