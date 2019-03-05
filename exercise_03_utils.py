from exercise_utils import Question, NoSolveQuestion
import textwrap

__all__ = [
            'q1a', 'q1b', 'q1c', 'q1d',
            'q2',
            'q3a', 'q3d',
            'q4b',
            'q5b', 'q5c', 'q5d',
            'q6a', 'q6b',
          ]

q1a = NoSolveQuestion(
        hint = textwrap.dedent(
            """ 
            
            """
        ))

q1b = NoSolveQuestion(
        hint = textwrap.dedent(
            """ 
            
            """
        ))

q1c = NoSolveQuestion(
        hint = textwrap.dedent(
            """ 
            Have a look on qutip's 
            [basis](http://qutip.org/docs/latest/apidoc/functions.html#qutip.states.basis)
            function.
            """
        ))

q1d = NoSolveQuestion(
        hint = textwrap.dedent(
            """ 
            C.f. krotov's documentation on 
            ['Using Krotov with QuTiP'](https://krotov.readthedocs.io/en/latest/07_qutip_usage.html).
            """
        ))


q2 = NoSolveQuestion(
        hint = textwrap.dedent(
            """ 
            Have a look on the documentation of krotov's
            [Objective class](https://krotov.readthedocs.io/en/stable/API/krotov.objectives.html#krotov.objectives.Objective).
            
            You will not need to specify the `c_ops` argument!
            The first three arguments are enough.
            """
        ))


q3a = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            **For the real pulses:**  
                Do not change *a*  in krotov.shapes.blackman and specify the
                pulses, such that they last from t=0 to 3 and from t=2 to ,
                respectively. The amplitude should be set to be the initial
                value.

            **For the imaginary pulses:**  
                Map the pulses to 0 for all *t*.
            """
        ))

q3d = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            The 'e_ops' argument in the mesolve function can be used to
            calculate the expectation values corresponding to states.
            If we just had projectors...
            """
        ))


q4b = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            Remember: the update is proportional to ${1}/{\lambda_a}$ 
            """
        ))


q5b = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            Does the phase of the final state matter?
            """
        ))

q5c = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            I think a fidelity (1-$J_{\mathrm{T}}$) of 99.9% is quite good.  
            And I think we should adjust the steps, to not wait longer than 
            2 min (for this first guess). Maybe give it a try and see how long
            a few steps take
            """
        ))

q5d = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            So let's see...  
            We give the `pulse_options` to krotov, which take some arguments
            that can be changed and we also have the `tlist`, which we can also
            vary. Also the parameters of the system can dramatically change the
            result of the initial guess and therefore also the optimization
            behavior. And now that you say it: The initial guess...

            So which of these changes would now be reasonable???
            """
        ))


q6a = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            Have a look on the optimized objectives
            (oct_result.optimized_objectives). And don't forget that you always
            have a list of objectives
            """
        ))

q6b = NoSolveQuestion(
        hint = textwrap.dedent(
            """
            You can access the $\mathrm{i}^{\mathrm{th}}th$ optimized control
            via 
            > `oct_result.optimized_controls[i]`
            """
        ))



