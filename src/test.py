import asyncio
import inverterLogger


def main():
    logger = inverterLogger.get_runtime_data()
    asyncio.run(logger)

main()