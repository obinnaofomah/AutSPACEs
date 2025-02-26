from django import forms

class UserProfileForm(forms.Form):

    autistic_identifications = [
        ("", "-----------"),
        ("yes", "Yes"),
        ("no", "No"),
        ("unspecified", "Prefer not to say"),
    ]
    autistic_identification = forms.ChoiceField(choices = autistic_identifications, widget = forms.Select(),
                                           label="Do you identify as autistic?",
                                           help_text="AutSPACEs is focusing on collecting and sharing the voices and lived experiences of autistic people, which is why this is a mandatory question. If you select <i>prefer not to say</i> your answers will be considered as coming from a non-autistic person, labeled as such and e.g. not used for research.",
                                           required=True)
    autistic_identification.group = 1
    autistic_identification.gap = True

    age_brackets = [
        ("18-25", "18-25"),
        ("26-35", "26-35"),
        ("36-45", "36-45"),
        ("46-65", "46-65"),
        ("over 65", "Over 65"),
        ("unspecified", "Prefer not to say"),
    ]
    age_bracket = forms.ChoiceField(choices = age_brackets, widget = forms.Select(), required=False,
                                   label="What is your age group?",
                                   help_text="Providing your age will help researchers understand potential trends across age groups. It will also help readers to better understand your perspective if this data is made public.",
                                   initial="unspecified")
    age_bracket.group = 1

    age_public = forms.BooleanField(label = "Make age public",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    age_public.group = 1
    age_public.gap = True

    genders = [
        ("nonbinary", "Non-binary"),
        ("female", "Female"),
        ("male", "Male"),
        ("self_identify", "Self identify"),
        ("unspecified", "Prefer not to say"),
    ]
    gender = forms.ChoiceField(choices = genders, widget = forms.Select(), required=False,
                              label="What gender do you identify with?",
                              help_text="Providing your gender identity will help researchers understand potential trends across this demographic. It will also help readers to better understand your perspective if this data is made public.",
                              initial="unspecified")
    gender.group = 1


    gender_self_identification = forms.CharField(label="Self identification",
                                 max_length=150, strip=True, required=False,
                                 widget=forms.TextInput())

    gender_self_identification.group = 1
    gender_self_identification.layout_horizontal = True

    gender_public = forms.BooleanField(label = "Make gender public",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))

    gender_public.group = 1
    gender_public.gap = True

    description = forms.CharField(label="What else would you like researchers (or readers) to know about yourself?",
                                 max_length=2048, strip=True, required=False,
                                 help_text="You can provide any additional context about yourself here that you deem relevant to understanding your perspective and experiences. The AutSPACEs team will potential use your information to refine the structured demographic questions above. You can also make this information publicly accessible &mdash; which will be linked to your public experiences.",
                                 widget=forms.Textarea(attrs={"placeholder":"Potential things you could talk about here include your ethnicity, whether you grew up/are living in a rural or urban environment, your educational background or really anything else that comes to your mind.",
                                                              "rows":"4",
                                                              "class":"form-control"}))
    description.group = 1

    description_public = forms.BooleanField(label = "Make description public",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    description_public.group = 1

    # Add triggering here
    abuse = forms.BooleanField(label = "Abuse (physical, sexual, emotional and verbal)",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    abuse.group = 2
    violence = forms.BooleanField(label = "Violence and Assault",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    violence.group = 2
    drug = forms.BooleanField(label = "Drug and/or Alcohol misuse",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    drug.group = 2
    mentalhealth = forms.BooleanField(label = "Mental Health Issues",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    mentalhealth.group = 2
    negbody = forms.BooleanField(label = "Negative body image",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    negbody.group = 2
    other = forms.BooleanField(label = "Other",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    other.group = 2

    # Communications preferences
    comms_review = forms.BooleanField(label = "When the review status of your story changes",
        required = False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    comms_review.group = 3

    # New user management
    profile_submitted = forms.BooleanField(label = "Profile submitted",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
    profile_submitted.group = "hidden"

class UserProfileDeleteForm(forms.Form):
    delete_oh_data = forms.BooleanField(label = "Delete your stories from OpenHumans",
                                       required=False,
                                       widget=forms.CheckboxInput(attrs={"class": "custom-control-input"}))
