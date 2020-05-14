# ReferralBot

Another small Discord bot i made.
The basic functionality is to count the number of referrals from different users.

Something cool i did with this project, is a dynamic configuration file parser.
You can specify the fields it should parse in `fields.json`


## Setup:
Config file should have the following format:

### config.json
```json
{
    "token": "[DISCORD_BOT_TOKEN]",
    "prefix": "[Whatever prefix you want]",
    "description": "[Bot description]",
    "name": "[Bot name]",
    "referral_levels": 
    {
        "[NUMBER_LEVEL1]": ROLE_ID1,
        "[NUMBER_LEVEL2]": ROLE_ID2
    }
}
```
