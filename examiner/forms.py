from django import forms

class addquestion(forms.Form):
	qid = forms.CharField(max_length=5)
	q = forms.CharField()
	opta = forms.CharField()
	optb = forms.CharField()
	optc = forms.CharField()
	optd = forms.CharField()
	answer = forms.CharField()

class addexam(forms.Form):
	examid = forms.CharField(max_length=5)
	examdate = forms.DateField()