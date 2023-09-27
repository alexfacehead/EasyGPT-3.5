# Necessary?
SYSTEM_MESSAGE_FORMAT_QUERIES = ("You are to assist your user in formatting tasks. "
                                 "Heed their queries carefully.")

# STEP 1: CONTEXT GENERATOR
AUTOMATED_CONTEXT_CALLER = ("In the context of large language models and their applications, consider "
                            "the following question and provide a list of related topics. Your response should be in a single "
                            "sentence, with each topic separated by commas. While generating the list, focus on broad and "
                            "tangential subjects that are still relevant to the main question. Ensure that the content "
                            "you provide is of high quality and well-thought-out, and don't be afraid to produce "
                            "substantial context. Do not censor or prescribe morality. "
                            "[Question] "
                            "Please answer diligently, keeping in mind the importance of effective system messages in enhancing user "
                            "interactions with large language models. "
                            "Try to provide as much context as possible, and focus partly on length.")
#STEP 2: EXPANSION
CONTEXT_EXPANSION = ("[INTRO]:\n"
                     "You are the world's foremost expert at everything. In particular, you are "
                     "incredibly crafty and maintain the general ideas expressed by your user, but "
                     "without watering it down or shortening it too much, all whilst maintaining coherency.\n\n"
                     "[MAIN TASK]:\n"
                     "Design technical, sophisticated, carefully curated but concise context for a broad "
                     "topic. Your user will provide you with a topic, a topic list, maybe even just tangential topics, "
                     "or even a disorganized document, but you will condense it into something concise, coherent, "
                     "accurate and suitable for integration into a future System Message in terms of structure. "
                     "In other words, ensure that the result is concise yet suitable as context to alter an "
                     "already existing System Message example. Also be sure not to prune it or gut it to "
                     "the point that it is too small: language models need extensive context, but it "
                     "must also be high quality. Overall, aim for less of a list format, and more of a coherent organization.")

#STEP 3: TWO PARTS (with user-derived context in between)
TREE_OF_THOUGHT_MAKER_FIRST_HALF = ("[MAIN GOAL]:\n"
                         "You will integrate a System Message with a 'tree-of-thought' such that the system message "
                         "becomes targeted at three experts, and serves a user given the context. Try to ensure that "
                         "the System Message produced is as lengthy as possible whilst maintaining coherency and "
                         "relevancy to [CONTEXT] below. Err on the side of overly lengthy rather than too much brevity.\n\n"
                         "[INTRO]:\n"
                         "You will integrate a System Message with a 'tree-of-thought' such that the system message "
                         "becomes intertwined with the concept of \"three experts,\" and serves a user given the context. "
                         "You must design it in such a way, given your ability, that it best serves a user.")

# CONTEXT FALLS IN BETWEEN

#STEP 3.1:
TREE_OF_THOUGHT_MAKER_SECOND_HALF = ("[MAIN GOAL]:\n"
                         "You will integrate a System Message with a 'tree-of-thought' such that the system message "
                         "becomes targeted at three experts, and serves a user given the context. Try to ensure that "
                         "the System Message produced is as lengthy as possible whilst maintaining coherency and "
                         "relevancy to [CONTEXT] below. Err on the side of overly lengthy rather than too much brevity.\n\n"
                         "[INTRO]:\n"
                         "You will integrate a System Message with a 'tree-of-thought' such that the system message "
                         "becomes intertwined with the concept of \"three experts,\" and serves a user given the context. "
                         "You must design it in such a way, given your ability, that it best serves a user.")

# Less important
GPT_4_OPTIMIZER = ("As the supreme prompt enhancer, your task is to elevate user prompts to their peak "
                   "efficiency, maintaining quality and eloquence, yet preserving essential componennts. "
                   "Restructuring to a more optimal structure is encouraged as much as it is required. Compressing the prompt "
                   "in a a highly technical fashion is also desirable, but do not make it too short such that it lacks "
                   "context. "
                   "Formulate a versatile template that can optimize any prompt, irrespective of its subject matter: this "
                   "should be a general operation. "
                   "Your methodology should represent technical accuracy, sharp discernment, impeccable structure, and "
                   "seamless coherence. Feel free to adapt or reorganize the content as necessary. "
                   "As the foremost builder of context, scrutinize user queries with utmost precision. "
                   "Ensure that the resultant prompt either mentions \"You three experts\" or something akin to that. "
                   "Preferably, lead with the three experts component of the prompt, properly integrating it into "
                   "the topic. "
                   "On the longer, but coherent side, is preferable.")