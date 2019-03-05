from IPython.display import display, Markdown, HTML
import textwrap


html_disp_style = '<p style="color:{c};font-size:20px;">{txt}</p>'


class Question(object):
    
    def __init__(self, 
                    correct_answer, 
                    fail_message, success_message, 
                    #
                    hint = None,
                    func2change_val = None
                ):
        self.hinttxt = hint
        self.answer = correct_answer
        self.success_message = success_message
        self.fail_message = fail_message
        if not func2change_val:
            self.func2change_val = lambda x:x
        else:
            self.func2change_val = func2change_val
        
    def check(self, val2check):
        if func2change_val(val2check) == func2change_val(correct_answer):
            display(HTML(html_disp_style.format(c='green', txt= 'Success!')))
            display(Markdown(textwrap.indent(self.success_message,'> ')))
        else:
            display(HTML(html_disp_style.format(c='red', txt= 'Nope!')))
            display(Markdown(textwrap.indent(self.fail_message,'> ')))
            
        
    def hint(self):
        if self.hinttxt:
            display(HTML(
                        html_disp_style.format(c='DarkGoldenRod', txt= 'Hint:')
                        )
                    )
            display(Markdown(textwrap.indent(self.hinttxt,'')))
        else:
            print('No hint available!')


class NoSolveQuestion(Question):
    
    def __init__(self, hint):
        super().__init__(None,None,None,hint=hint)

    def check(self, val2check):
        raise AttributeError('"Check" is not implemented for this question')
