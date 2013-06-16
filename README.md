plivo-ivr-creator
=================

An application that creates an ivr service based on the json  given as input to it.


**Installation**

Clone the repository:
```
git clone git@github.com:saadbinakhlaq/plivo-ivr-creator.git
```

Install the dependencies:
```
pip install -r requirements.txt
```

* Update auth    _id and auth    _token and the url with your own id, token and url in the ivr file


**IVR Input**
This is a json string something like in this format
```
{
  "message": "for x press 1 for y press 2",
	"actions": {
				1: {
					"message": "for a press 1 for b press 2",
					"actions": {
								1: {"message": "you are in 1",
									"actions": None},
								2: {"message": "you are in 2",
									"actions": None}
								},
					},
				2: {
					"message": "for c press 5 for d press 6",
					"actions": {
								5: {"message": "you are in 5",
									"actions": None},
								6: {"message": "you are in 6",
									"actions": None}

								},
					}

			}
}```

**Phone Number Input**
Specify the phone number to be called here in this format. Country code 1st without any + or 00 for e.g. Indian phone number 919XXXXXXXXX
