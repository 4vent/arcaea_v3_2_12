import re
import sys
sys.path.append('.')
from corresponds import corres, spaces, num2char
from colordprint import colordprint

from ARGTool import arc_cripted_text_braker, combination_generator

cripted_texts = [
    # "The World of Arcaea welcomes all.",
    # "",
    "bO3ueWuP,3b4fEK4GVeO4vVe3VOD.",
    "bO4ueWuP,3b4fEK7GVeO7vVe3_VWOuhDKK4VuPDeK.",
    "",
    "dV,3b3eDvWKD",
    "b7eDvWKD4uV7hDu4Ehh4vEjD4EfEq...",
    "",
    "BPiK7XVi_D4b'XD7WKDj4uV4_Ehh7WrVO4KV3nEOq3VuPDeK...",
    "...iK7iu4eDE_PiOU3qVW?",
    "",
    "bv4qVW3PDEe3nD...",
    "hiKuDO,4EOj7E_u...",
    "",
    "BPD3rEKu4DliKuK,4uPDeDvVeD3vEuD4_EO3GD7VXDeuWeODj.",
    "IVW4DliKu3OVf4hVOU4EvuDe3vEuD7PEK4ueEOKrieDj.",
    "",
    "BPiK3iK3OV3rhE_D4uV7KW__WnG4uV3ueEUDjq",
    "aivD,4DliKuDO_D,3iK3PVrD-vWhh",
    "",
    "ZiKD7OVf,7EOj3iO4UhEKK7b4fihh4eDnDnGDe4qVW.",
    "ZiKD7OVf,7EOj3iO4UhEKK7b4fihh4eDnDnGDGDe4qVW."
]

# cripted_texts += ["", ' '.join(combination_generator(num2char))]
        
ACTB = arc_cripted_text_braker(corres, spaces)

for cripted_text in cripted_texts:
    plain_text = ACTB.decript(cripted_text, with_num=False, kvswap=False)
    nums = '\033[99m' + ACTB.get_space_letters(cripted_text) + '\033[0m'

    colordprint(
        plain_text,
        colorful_strength=0.08,
        customcolor=(1.0, 0.4, 0.55)
    )
    colordprint(nums, customcolor=(0.5, 0.5, 0.5))

# print('')
# tmp = "The World of Arcaea welcomes all."
# for _ in range(4):
#     tmp = ACTB.decript(tmp, kvswap=False)
#     print(tmp)
#     tmp = re.sub(r'\033\[[0-9]+m', '', tmp)
