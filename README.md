# Move Tabs Anywhere #

A [Sublime Text 3](http://www.sublimetext.com/3) plugin that allows you to move tabs anywhere with your keyboard.

This plugin was created because of the weird behavior in ST3 when trying to move the tabs manually.  
Also, keyboard shortcuts are awesome!

![Animated GIF of quirk](http://i.imgur.com/ZnHAvx4.gif "This is annoying")

---

## Usage ##

##### OSX ######

| Key Binding | Action |
| --- | --- |
| ⌘+K, ⌘+comma  | move this tab to the left |
| ⌘+K, ⌘+period | move this tab to the right |

##### Windows & Linux ######

| Key Binding | Action |
| --- | --- |
| Ctrl+K, Ctrl+comma  | move this tab to the left |
| Ctrl+K, Ctrl+period | move this tab to the right |

#### Recommended Key Bindings ####

**Note:** These key binding will override the default code folding behavior.  
To use, rename `Example ([OS]).sublime-keymap` to `Default ([OS]).sublime-keymap`

##### OSX ######

| Key Binding | Action |
| --- | --- |
| ⌘+K, ⌘+[digit] | move this tab anywhere in the group |

##### Windows & Linux ######

| Key Binding | Action |
| --- | --- |
| Ctrl+K, Ctrl+[digit] | move this tab anywhere in the group |

## Changelog ##

#### v1.0.1 ####

* No longer overriding default key bindings.
* Changed name to reflect how it stands out from other similar plugins.
* Refactored move logic.

#### v1.0.0 ####

* Initial release.

## License ##

Copyright (c) 2014 Ilya Kaminsky

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
