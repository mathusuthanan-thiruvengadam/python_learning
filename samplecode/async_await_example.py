import asyncio

async def openfile(filename):
    return open(filename, 'r')

async def read(filehandle):
    return filehandle.read()

async def read_data_from_file(filename):
    filehandle = await openfile(filename)
    data = await read(filehandle)
    return data

async def main():
    file1data = read_data_from_file("sampledata1.txt")
    file2data = read_data_from_file("sampledata2.txt")
    file3data = read_data_from_file("sampledata3.txt")
    file4data = read_data_from_file("sampledata4.txt")

    # Gather the results
    results = await asyncio.gather(file1data, file2data, file3data, file4data)
    return results

async def run_main():
    result = await main()
    print(''.join(result))  # Concatenate and print the results

asyncio.run(run_main())  # Run the main function
