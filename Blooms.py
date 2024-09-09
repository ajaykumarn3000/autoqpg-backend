"""
This File contains the implementation of the Bloom's Taxonomy.
For Accuracy, use the keywords in the question as mentioned in the taxonomy_keywords dictionary.
The function get_taxonomy_level(question) returns the Bloom's Taxonomy level of the question.
"""


#This taxonomy_keywords dictionary contains a list of keywords for each level of Bloom's Taxonomy.
taxonomy_keywords = {
    "BL1": [
        "define", "list", "name", "recall", "recognize", "identify", "describe", 
        "who", "what", "where", "when", "label", "recite", "select", "repeat", 
        "state", "find", "match", "outline", "choose"
    ],
    "BL2": [
        "explain", "summarize", "paraphrase", "interpret", "classify", 
        "compare", "contrast", "discuss", "describe", "exemplify", "infer", 
        "conclude", "predict", "translate", "generalize", "illustrate", 
        "differentiate", "express", "estimate", "review"
    ],
    "BL3": [
        "apply", "solve", "use", "demonstrate", "calculate", "implement", 
        "execute", "perform", "construct", "operate", "show", "practice", 
        "employ", "manipulate", "illustrate", "model", "interpret", "schedule", 
        "plan", "prepare", "modify"
    ],
    "BL4": [
        "analyze", "differentiate", "organize", "relate", "compare", 
        "contrast", "examine", "break down", "dissect", "distinguish", 
        "separate", "categorize", "classify", "order", "prioritize", 
        "infer", "attribute", "investigate", "appraise"
    ],
    "BL5": [
        "evaluate", "critique", "assess", "judge", "defend", "justify", 
        "support", "argue", "rate", "validate", "verify", "select", 
        "explain", "estimate", "criticize", "measure", "appraise", 
        "conclude", "check", "prioritize", "recommend"
    ],
    "BL6": [
        "create", "design", "construct", "plan", "produce", "invent", 
        "develop", "generate", "compose", "synthesize", "formulate", 
        "propose", "assemble", "build", "integrate", "organize", 
        "devise", "modify", "brainstorm", "predict", "hypothesize"
    ]
}


"""
This function takes a question as input and returns the Bloom's Taxonomy level of the question.
    :param question: The question for which the Bloom's Taxonomy level is to be determined.
    :return: The Bloom's Taxonomy level of the question.

"""
def get_taxonomy_level(question):
    question = question.lower().strip()
    
    
    if "find" in question:
        if any(word in question for word in ["who", "what", "when", "where"]):
            return "BL1"
        else:
            return "BL3"

    if "identify" in question:
        if any(word in question for word in ["list", "name", "recall"]):
            return "BL1"
        else:
            return "BL4"

    if "compare" in question or "contrast" in question:
        return "BL4"

    if "solve" in question:
        return "BL3"

    
    if any(phrase in question for phrase in ["tell me about", "can you explain"]):
        return "BL2"

   
    for level, keywords in taxonomy_keywords.items():
        for keyword in keywords:
            if keyword in question:
               
                if keyword == "describe":
                    if any(word in question for word in ["compare", "contrast"]):
                        return "BL4"
                    elif any(word in question for word in ["example", "illustrate"]):
                        return "BL3"
                    return "BL2"
                
                if keyword == "illustrate" and ("apply" in question or "example" in question):
                    return "BL3"
                if keyword == "construct" and ("design" in question or "create" in question):
                    return "BL6"
                
                return level
    
   
    return "Not classified"