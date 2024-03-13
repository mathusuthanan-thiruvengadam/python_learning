import asyncio
import aiofiles

async def read_file_contents(filename):
    filehandle = await aiofiles.open(filename,"r")
    data = await filehandle.read()
    return data

async def printdata(filename):
    data = await read_file_contents(filename)
    print(data)


asyncio.run (printdata("sampledata1.txt"))
