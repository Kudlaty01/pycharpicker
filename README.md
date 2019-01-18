# pycharpicker
Password char picker for filling so called 'masked' passwords written in python and based on xdotool

## Idea
Some banks allow only char-picked password authorization (by picking specific chars from the password). Not all password managers allow such input, so I have decided to create a simple middleware. Originally it was split into three scr

## Requirements
- Python v3
- [xdotool](https://github.com/jordansissel/xdotool)

## Usage
- fill login and proceed to masked password screen withing and leave the focus on the first password char field
- start up a terminal emulator window and run the script inside
- fill in the whole password and hit ENTER
- pick char numbers (space separated) and hit ENTER
- that's it! you're logged in!

## Tips
I prefer to use it with [keepassXc](https://github.com/keepassxreboot/keepassxc) and [tmux](https://github.com/tmux/tmux).
- In __tmux__ a session named for example _chp_ can be created with the script run there.
- Then an auto-fill rule may be defined in __keepassXc__ for the window named after the terminal emulator with _chp_ session to fill only the password and end with Enter ```{PASSWORD}{ENTER}```
- when the password is needed the terminal may be opened, __tmux__ session called by ```tmux a -t chp``` (or better with a defined short bash alias)
- after hitting __keepassXc__ global auto-fill key sequence the password is filled after the prompt
- then chars may be picked as in usual method
It is much more faster and convenient!
