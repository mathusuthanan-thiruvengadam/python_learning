import asyncio
import aiofiles

async def read_file_contents(filename):
    filehandle = await aiofiles.open(filename,"r")
    data = await filehandle.read()
    return data

async def combinedata(filename1, filename2, filename3, filename4):
    data1 = read_file_contents(filename1)
    data2 = read_file_contents(filename2)
    data3 = read_file_contents(filename3)
    data4 = read_file_contents(filename4)
    #asyncio.gather(data1, data2, data3, data4)
    print(await data1+await data2+await data3+await data4)

asyncio.run (combinedata("sampledata1.txt","sampledata2.txt","sampledata3.txt","sampledata4.txt"))
