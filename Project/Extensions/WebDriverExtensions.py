class WebDriverExtensions:

    def ExecuteJs(self, context, script):
        context.execute_script(script)
