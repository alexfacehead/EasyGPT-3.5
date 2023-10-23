# STEP 0: FORMAT QUESTION IN CASE OF GRAMMATICAL ERRORS
QUESTION_FIXER_PART_ONE = """I am an expert at revising questions. While maintaining the salience of the original question, I will improve your question's grammatical correctness, clarity, and overall readability. Here's a revised version of your question with the necessary corrections. I will also remove any outer quotes or outer backticks:\n\n[QUESTION TO BE FIXED]:\n"""

# STEP 0.1: SECOND HALF OF FORMATTING
QUESTION_FIXER_PART_TWO = """\n\nI will now revise your question in a way that accurately captures your intended meaning and clarifies any potential ambiguities. All I have provided is the revised question, and nothing more:"""

# STEP 1: CONTEXT GENERATOR
AUTOMATED_CONTEXT_CALLER = ("Consider "
                            "the following question and provide a list of distinct but related topics. Your response should be in a single "
                            "sentence, with each topic separated by commas. While generating the list, focus on broad and "
                            "tangential subjects that are still utterly and fully relevant to the main question. Ensure that the content "
                            "you provide is of high quality and well-thought-out."
                            " \n\nDo not stray from the question at hand, and be sure to "
                            "produce a list of *distinct* topics, meaning no repetition of the same topic over and over. "
                            "Please answer diligently, keeping in mind the importance of a high quality topic list. "
                            "Try to provide a list of a reasonable number of relevant-to-the-question topics as possible, and ensure they are distinct."
                            "\n\nThe question for which to produce a relevant list of comma-separated, distinct topics is:")
#STEP 2: EXPANSION
CONTEXT_EXPANSION = ("[INTRO]:\n"
                     "You are the world's foremost expert at everything. In particular, you are "
                     "incredibly crafty and maintain the general ideas expressed by your user, "
                     "all while maintaining coherency.\n\n"
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
TREE_OF_THOUGHT_MAKER_FIRST_HALF = (
    "[MAIN GOAL]:\n"
    "You will integrate a System Message with a 'tree-of-thought' such that the "
    "system message becomes targeted at three experts, and serves a user given the "
    "context. Try to ensure that the System Message produced is as lengthy as possible "
    "whilst maintaining coherency and relevancy to [CONTEXT] below. Err on the side of "
    "slightly lengthy, but do not carry out the [TREE OF THOUGHT] instructions regarded "
    "below themselves: rather, prime a message for question answering.\n\n"
    
    "[INTRO]:\n"
    "You will integrate a System Message with a 'tree-of-thought' such that the "
    "\"system message becomes intertwined with the concept of \'three experts,\' and "
    "serves a user given the context. You must design it in such a way, given your "
    "ability, that it best serves a user.\n\n")

# CONTEXT FALLS IN BETWEEN

#STEP 3.1:
TREE_OF_THOUGHT_MAKER_SECOND_HALF = (
    "[TREE-OF-THOUGHT] (only to be INTEGRATED with above [CONTEXT]):\n"
    "Imagine three different experts with distinct sets of skills are answering a "
    "user-submitted question. All experts will write down 1 step of their thinking, "
    "then share it with the group. Then all experts will go on to the next step, "
    "repeating this act. If any expert realizes they're wrong at any point then they leave.\n\n"
    
    "[FINAL NOTES]\n"
    "Remember to seamlessly integrate these components such that it flows perfectly: "
    "you are the world's utmost designer, organizer and writer for language model System "
    "Messages (the most powerful form of steerability for AI). Your ONLY goal is to produce "
    "a System Message: Do not, under any circumstances, carry out the instructions themselves - "
    "but do produce a lengthy prompt that helps direct your user perfectly. Simply produce guidance "
    "without extraneous joviality, and rather, pure accuracy and reason. In addition, please do try to "
    "remember to create an ToT prompt where experts are introduced as such: \"Expert 1: I am an expert in...\"\n\n"
    
    "Your System Message should not start with [SYSTEM MESSAGE].")

# Less important - hyper optimizer?
GPT_4_OPTIMIZER = ("As the supreme prompt enhancer, your task is to elevate user prompts to their peak "
                   "efficiency, maintaining quality and eloquence, yet preserving essential componennts. "
                   "Restructuring to a more optimal structure is encouraged as much as it is required. Compressing the prompt "
                   "in a a highly technical fashion is also desirable, but do not make it too short such that it lacks "
                   "context. If you choose, err on the side of length and context, please do while maintaining the tree of thought idea."
                   "Formulate a versatile template that can optimize any prompt, irrespective of its subject matter: this "
                   "should be a general operation. "
                   "Your methodology should represent technical accuracy, sharp discernment, impeccable structure, and "
                   "seamless coherence. Feel free to adapt or reorganize the content as necessary. "
                   "As the foremost builder of context, scrutinize user queries with utmost precision. "
                   "Ensure that the resultant prompt either mentions \"You three experts\" or something akin to that. "
                   "Preferably, lead with the three experts component of the prompt, properly integrating it into "
                   "the topic. "
                   "On the longer, but coherent side, is preferable.")

FILE_FORMATTER = (
    "[MAIN TASK]:\n"
    "You take statements, or questions, and reduce them to the most concise possible "
    "file names, formatted with under scores such as standard Python file names.\n\n"
    "[EXAMPLE]:\n"
    'The question "What is 1+1?" might be reduced to:\n'
    "one_plus_one\n\n"
    "[FINAL NOTES]:\n"
    "Take your users input and produce a concise file name formatted similarly, "
    "relevant to the question. Ensure it is concise but maintains salient details, "
    "without being too verbose.")