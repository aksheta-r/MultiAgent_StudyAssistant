def router_agent(task):

    if task == "Explain Topic":
        return "explainer"

    elif task == "Generate Summary":
        return "summary"

    elif task == "Generate Quiz":
        return "quiz"