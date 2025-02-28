import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.joinpath("..")))

from clickthebutton.responses import FOUGHT_OFF, SINGULAR_FOUGHT_OFF

DYNAMIC_ONLY = True


async def main():
    for verb in FOUGHT_OFF + SINGULAR_FOUGHT_OFF:
        if type(verb) is tuple:
            parts = []
            for part in verb:
                if callable(part):
                    part = part()
                    if asyncio.iscoroutine(part):
                        part = await part
                    parts.append(str(part))
                else:
                    parts.append(part)
            verb = "".join(parts)
            print(verb)
        elif not DYNAMIC_ONLY:
            print(verb)


if __name__ == "__main__":
    asyncio.run(main())
