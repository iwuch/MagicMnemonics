# -*- coding: utf-8 -*-
from wox import Wox
from utils import *

class MagicMnemonics(Wox):
    # query is default function to receive realtime keystrokes from wox launcher
    def query(self, query):
        results = []
        rets = get_harmonic(query) if len(query)>=2 else reminder
        for ret in rets:
            results.append({
                # "Title": "Type 2-6 alphabets, you will get a Chinese name.",
                "Title": "谐音记忆法: {}".format(ret['name']),
                "SubTitle": "Story: {}".format(ret['story']),
                "IcoPath":"Images/app.png",
                "ContextData": "ctxData",
                "JsonRPCAction": {
                    'method': 'take_action',
                    'parameters': ["{}".format("SomeData")],
                    'dontHideAfterAction': False
                }
            })
        return results
    # context_menu is default function called for ContextData where `data = ctxData`

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.png"
        })
        return results

    def take_action(self, SomeArgument):
        # Choose what to trigger on pressing enter on the result.
        # use SomeArgument to do something with data sent by parameters.
        return None

if __name__ == "__main__":
    MagicMnemonics()
