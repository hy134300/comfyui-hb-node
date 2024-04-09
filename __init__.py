import asyncio
import json
import os
import sys

from custom_nodes.ComfyUI_Sound_NODE.huiben import generate, contactText, batch, qianwen, saveImage

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

import folder_paths

from custom_nodes.ComfyUI_Comfyroll_CustomNodes.nodes.nodes_utils_text import AnyType

ORDER_MAP = ['zh-CN-YunxiNeural', 'zu-ZA-ThembaNeural', 'zu-ZA-ThandoNeural', 'zh-TW-YunJheNeural',
             'zh-TW-HsiaoYuNeural',
             'zh-TW-HsiaoChenNeural', 'zh-HK-WanLungNeural', 'zh-HK-HiuMaanNeural', 'zh-HK-HiuGaaiNeural',
             'zh-CN-shaanxi-XiaoniNeural', 'zh-CN-liaoning-XiaobeiNeural', 'zh-CN-YunyangNeural', 'zh-CN-YunxiaNeural',
             'zh-CN-YunjianNeural', 'zh-CN-XiaoyiNeural', 'zh-CN-XiaoxiaoNeural',
             'en-US-SteffanNeural', 'en-US-RogerNeural', 'en-US-MichelleNeural', 'en-US-JennyNeural', 'en-US-GuyNeural',
             'en-US-EricNeural', 'en-US-EmmaNeural', 'en-US-EmmaMultilingualNeural', 'en-US-ChristopherNeural',
             'en-US-BrianNeural', 'en-US-BrianMultilingualNeural', 'en-US-AvaNeural', 'en-US-AvaMultilingualNeural',
             'en-US-AriaNeural', 'en-US-AndrewNeural', 'en-US-AndrewMultilingualNeural']

TEXT_TYPE = "STRING"
any_type = AnyType("*")

class SoundVoice:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "voice": (ORDER_MAP,),
                "filename_prefix": ("STRING", {"default": "sound"}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('outdir',)
    FUNCTION = 'sound'
    CATEGORY = 'utils'

    def sound(self, text, voice, filename_prefix):
        asyncio.run(generate(text, voice, "output/" + filename_prefix + ".mp3"))
        return (filename_prefix + ".mp3",)


class LatenToList:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"image": ("IMAGE",), }
                }

    RETURN_TYPES = ("IMAGE", "IMAGE", "IMAGE", "IMAGE",
                    "IMAGE", "IMAGE", "IMAGE", "IMAGE",
                    "IMAGE", "IMAGE", "IMAGE", "IMAGE",
                    "IMAGE", "IMAGE", "IMAGE", "IMAGE",
                    "IMAGE", "IMAGE", "IMAGE", "IMAGE",)
    RETURN_NAMES = ("string_1", "string_2", "string_3", "string_4",
                    "string_5", "string_6", "string_7", "string_8",
                    "string_9", "string_10", "string_11", "string_12",
                    "string_13", "string_14", "string_15", "string_16",
                    "string_17", "string_18", "string_19", "string_20",)
    FUNCTION = 'foreach'
    CATEGORY = 'image'

    def foreach(self, image):
        results1 = []
        results2 = []
        results3 = []
        results4 = []
        results5 = []
        results6 = []
        results7 = []
        results8 = []
        results9 = []
        results10 = []
        results11 = []
        results12 = []
        results13 = []
        results14 = []
        results15 = []
        results16 = []
        results17 = []
        results18 = []
        results19 = []
        results20 = []
        results1.append(image[0])
        string_1 = results1
        results2.append(image[1])
        string_2 = results2
        results3.append(image[2])
        string_3 = results3
        results4.append(image[3])
        string_4 = results4
        results5.append(image[4])
        string_5 = results5
        results6.append(image[5])
        string_6 = results6
        results7.append(image[6])
        string_7 = results7
        results8.append(image[7])
        string_8 = results8
        results9.append(image[8])
        string_9 = results9
        results10.append(image[9])
        string_10 = results10
        results11.append(image[10])
        string_11 = results11
        results12.append(image[11])
        string_12 = results12
        results13.append(image[12])
        string_13 = results13
        results14.append(image[13])
        string_14 = results14
        results15.append(image[14])
        string_15 = results15
        results16.append(image[15])
        string_16 = results16
        results17.append(image[16])
        string_17 = results17
        results18.append(image[17])
        string_18 = results18
        results19.append(image[18])
        string_19 = results19
        results20.append(image[19])
        string_20 = results20

        return (string_1, string_2, string_3, string_4, string_5, string_6, string_7, string_8,
                string_9, string_10, string_11, string_12, string_13, string_14, string_15, string_16
                , string_17, string_18, string_19, string_20,)


class TextConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "delimiter": ("STRING", {"default": ", "}),
                "clean_whitespace": (["true", "false"],),
            },
            "optional": {
                "text_0": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_1": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_2": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_3": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_4": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_5": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_6": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_7": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_8": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_9": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_10": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_11": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_12": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_13": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_14": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_15": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_16": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_17": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_18": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),
                "text_19": (TEXT_TYPE, {"forceInput": (True if TEXT_TYPE == 'STRING' else False)}),

            }
        }

    RETURN_TYPES = (TEXT_TYPE,)
    FUNCTION = "text_concatenate"

    CATEGORY = "text"

    def text_concatenate(self, delimiter, clean_whitespace, **kwargs):
        merged_text = contactText(clean_whitespace, delimiter, kwargs)
        return (merged_text,)

class MovieGenerate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image_dir": ("STRING", {"default": "", "multiline": True}),
                "sound_dir": ("STRING", {"default": "", "multiline": True}),
                "output_name": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('outdir',)
    FUNCTION = 'movie'
    CATEGORY = 'utils'

    def movie(self, image_dir, sound_dir, output_name):
        generate(image_dir, sound_dir, output_name)
        return (image_dir,)



class MovieBatch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "movie_name": ("STRING", {"default": "last", "multiline": True}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('outdir',)
    FUNCTION = 'generate'
    CATEGORY = 'utils'

    def generate(self, movie_name):
        batch( movie_name)
        return (1,)

class HySaveImage:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"images": ("IMAGE", ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"})},
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('outdir',)
    FUNCTION = "save_images"
    CATEGORY = 'image'

    def save_images(self, images, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None):
        return saveImage(extra_pnginfo, filename_prefix, images, prompt)




class GenerateStroy:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "apiKey": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('text_positive',)
    FUNCTION = 'generate'
    CATEGORY = 'utils'

    def generate(self, text, apiKey):
        return qianwen(apiKey, text)




# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "sound voice": SoundVoice,
    "text concat": TextConcat,
    "latent to list": LatenToList,
    "movie generate": MovieGenerate,
    "movie batch": MovieBatch,
    "hy save image": HySaveImage,
    "generate story": GenerateStroy



}
