from typing import Literal

import helium
from typing import Callable


class HeliumElements:
    def __init__(self) -> None:
        self.Alert: helium.Alert = helium.Alert
        """Lets you identify and interact with JavaScript alert boxes."""
        self.Button: helium.Button = helium.Button
        """
	Lets you identify a button on a web page. A typical usage of ``Button`` is::

		click(Button("Log In"))

	``Button`` also lets you read a button's properties. For example, the
	following snippet clicks button "OK" only if it exists::

		if Button("OK").exists():
		    click(Button("OK"))

	When there are multiple occurrences of a button on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Button("Log In", below=TextField("Password")))
	"""
        self.CheckBox: helium.CheckBox = helium.CheckBox
        """
	Lets you identify a check box on a web page. To tick a currently unselected
	check box, use::

		click(CheckBox("I agree"))

	``CheckBox`` also lets you read the properties of a check box. For example,
	the method :py:func:`CheckBox.is_checked` can be used to only click a check
	box if it isn't already checked::

		if not CheckBox("I agree").is_checked():
		    click(CheckBox("I agree"))

	When there are multiple occurrences of a check box on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(CheckBox("Stay signed in", below=Button("Sign in")))
	"""
        self.ComboBox: helium.ComboBox = helium.ComboBox
        """
	Lets you identify a combo box on a web page. This can for instance be used
	to determine the current value of a combo box::

		ComboBox("Language").value

	A ComboBox may be *editable*, which means that it is possible to type in
	arbitrary values in addition to selecting from a predefined drop-down list
	of values. The property :py:func:`ComboBox.is_editable` can be used to
	determine whether this is the case for a particular combo box instance.

	When there are multiple occurrences of a combo box on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		select(ComboBox(to_right_of="John Doe", below="Status"), "Active")

	This sets the Status of John Doe to Active on the page.
	"""
        self.Image: helium.Image = helium.Image
        """
	Lets you identify an image (HTML ``<img>`` element) on a web page.
	Typically, this is done via the image's alt text. For instance::

		click(Image(alt="Helium Logo"))

	You can also query an image's properties. For example, the following snippet
	clicks on the image with alt text "Helium Logo" only if it exists::

		if Image("Helium Logo").exists():
		    click(Image("Helium Logo"))

	When there are multiple occurrences of an image on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Image("Helium Logo", to_left_of=ListItem("Download")))
	"""
        self.Link: helium.Link = helium.Link
        """
	Lets you identify a link on a web page. A typical usage of ``Link`` is::

		click(Link("Sign in"))

	You can also read a ``Link``'s properties. This is most typically used to
	check for a link's existence before clicking on it::

		if Link("Sign in").exists():
		    click(Link("Sign in"))

	When there are multiple occurrences of a link on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(Link("Block User", to_right_of="John Doe"))
	"""
        self.ListItem: helium.ListItem = helium.ListItem
        """
	Lets you identify a list item (HTML ``<li>`` element) on a web page. This is
	often useful for interacting with elements of a navigation bar::

		click(ListItem("News Feed"))

	In other cases such as an automated test, you might want to query the
	properties of a ``ListItem``. For example, the following line checks whether
	a list item with text "List item 1" exists, and raises an error if not::

		assert ListItem("List item 1").exists()

	When there are multiple occurrences of a list item on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(ListItem("List item 1", below="My first list:"))
	"""
        self.RadioButton: helium.RadioButton = helium.RadioButton
        """
	Lets you identify a radio button on a web page. To select a currently
	unselected radio button, use::

		click(RadioButton("Windows"))

	``RadioButton`` also lets you read the properties of a radio button. For
	example, the method :py:func:`RadioButton.is_selected` can be used to only
	click a radio button if it isn't already selected::

		if not RadioButton("Windows").is_selected():
		    click(RadioButton("Windows"))

	When there are multiple occurrences of a radio button on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		click(RadioButton("I accept", below="License Agreement"))
	"""
        self.Text: helium.Text = helium.Text
        """
	Lets you identify any text or label on a web page. This is most useful for
	checking whether a particular text exists::

		if Text("Do you want to proceed?").exists():
		    click("Yes")

	``Text`` also makes it possible to read plain text data from a web page. For
	example, suppose you have a table of people's email addresses. Then you
	can read John's email addresses as follows::

		Text(below="Email", to_right_of="John").value

	Similarly to ``below`` and ``to_right_of``, the keyword parameters ``above``
	and ``to_left_of`` can be used to search for texts above and to the left of
	other web elements.
	"""
        self.TextField: helium.TextField = helium.TextField
        """
	Lets you identify a text field on a web page. This is most typically done to
	read the value of a text field. For example::

		TextField("First name").value

	This returns the value of the "First name" text field. If it is empty, the
	empty string "" is returned.

	When there are multiple occurrences of a text field on a page, you can
	disambiguate between them using the keyword parameters ``below``,
	``to_right_of``, ``above`` and ``to_left_of``. For instance::

		TextField("Address line 1", below="Billing Address:").value
	"""
        self.find_all: Callable = helium.find_all
        """
	Lets you find all occurrences of the given GUI element predicate. For
	instance, the following statement returns a list of all buttons with label
	"Open"::

		find_all(Button("Open"))

	Other examples are::

		find_all(Window())
		find_all(TextField("Address line 1"))

	The function returns a list of elements of the same type as the passed-in
	parameter. For instance, ``find_all(Button(...))`` yields a list whose
	elements are of type :py:class:`Button`.

	In a typical usage scenario, you want to pick out one of the occurrences
	returned by :py:func:`find_all`. In such cases, :py:func:`list.sort` can
	be very useful. For example, to find the leftmost "Open" button, you can
	write::

		buttons = find_all(Button("Open"))
		leftmost_button = sorted(buttons, key=lambda button: button.x)[0]
	"""

    def __str__(self) -> str:
        return "Collection of Elements Selector from `helium` module"

    def __repr__(self) -> str:
        return self.__str__()


class MouseActions:
    def __init__(self) -> None:
        self.click: Callable = helium.click
        """
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Clicks on the given element or point. Common examples are::

		click("Sign in")
		click(Button("OK"))
		click(Point(200, 300))
		click(ComboBox("File type").top_left + (50, 0))
	"""
        self.doubleclick: Callable = helium.doubleclick
        """
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Performs a double-click on the given element or point. For example::

		doubleclick("Double click here")
		doubleclick(Image("Directories"))
		doubleclick(Point(200, 300))
		doubleclick(TextField("Username").top_left - (0, 20))
	"""
        self.drag: Callable = helium.drag
        """
	:param element: The element or point to drag.
	:type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`
	:param to: The element or point to drag to.
	:type to: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Drags the given element or point to the given location. For example::

		drag("Drag me!", to="Drop here.")

	The dragging is performed by hovering the mouse cursor over ``element``,
	pressing and holding the left mouse button, moving the mouse cursor over
	``to``, and then releasing the left mouse button again.

	This function is exclusively used for dragging elements inside one web page.
	If you wish to drag a file from the hard disk onto the browser window (eg.
	to initiate a file upload), use function :py:func:`drag_file`.
	"""
        self.press_mouse_on: Callable = helium.press_mouse_on
        self.release_mouse_over: Callable = helium.release_mouse_over
        self.rightclick: Callable = helium.rightclick
        """
	:param element: The element or point to click.
	:type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Performs a right click on the given element or point. For example::

		rightclick("Something")
		rightclick(Point(200, 300))
		rightclick(Image("captcha"))
	"""

    @staticmethod
    def scroll(
        direction: Literal["up", "down", "left", "right"] = "down",
        num_pixels: int = 100,
    ):
        """Scrolls in the specified direction, for the given number of pixels"""
        match direction.casefold().strip():
            case "up":
                helium.scroll_up(num_pixels=num_pixels)
            case "down":
                helium.scroll_down(num_pixels=num_pixels)
            case "left":
                helium.scroll_left(num_pixels=num_pixels)
            case "right":
                helium.scroll_right(num_pixels=num_pixels)

    def __str__(self) -> str:
        return "Collection of Mouse Actions from `helium` module"

    def __repr__(self) -> str:
        return self.__str__()


class HeliumActions:
    def __init__(self):
        self.highlight = helium.highlight
        """
	:param element: The element to highlight.

	Highlights the given element on the webpage by drawing a red rectangle
	around it. This is useful for debugging purposes. For example::

		highlight("Helium")
		highlight(Button("Sign in"))
	"""
        self.wait_until = helium.wait_until
        """
	:param condition_fn: A function taking no arguments that represents the \
	condition to be waited for.
	:param timeout_secs: The timeout, in seconds, after which the condition is \
	deemed to have failed.
	:param interval_secs: The interval, in seconds, at which the condition \
	function is polled to determine whether the wait has succeeded.

	Waits until the given condition function evaluates to true. This is most
	commonly used to wait for an element to exist::

		wait_until(Text("Finished!").exists)

	More elaborate conditions are also possible using Python lambda
	expressions. For instance, to wait until a text no longer exists::

		wait_until(lambda: not Text("Uploading...").exists())

	``wait_until`` raises
	:py:class:`selenium.common.exceptions.TimeoutException` if the condition is
	not satisfied within the given number of seconds. The parameter
	``interval_secs`` specifies the number of seconds Helium waits between
	evaluating the condition function.
	"""
        self.refresh = helium.refresh
        """
	Refreshes the current page. If an alert dialog is open, then Helium first
	closes it.
	"""
        self.attach_file = helium.attach_file
        """
	:param file_path: The path of the file to be attached.
	:param to: The file input element to which the file should be attached.

	Allows attaching a file to a file input element. For instance::

		attach_file("c:/test.txt", to="Please select a file:")

	The file input element is identified by its label. If you omit the ``to=``
	parameter, then Helium attaches the file to the first file input element it
	finds on the page.
	"""
        self.drag_file = helium.drag_file
        """
	Simulates the dragging of a file from the computer over the browser window
	and dropping it over the given element. This allows, for example, to attach
	files to emails in Gmail::

		click("COMPOSE")
		write("example@gmail.com", into="To")
		write("Email subject", into="Subject")
		drag_file(r"C:\\Documents\\notes.txt", to="Drop files here")
	"""
        self.combobox_select = helium.select
        """
	:param combo_box: The combo box whose value should be changed.
	:type combo_box: str, unicode or :py:class:`ComboBox`
	:param value: The visible value of the combo box to be selected.

	Selects a value from a combo box. For example::

		select("Language", "English")
		select(ComboBox("Language"), "English")
	"""
        self.hover = helium.hover
        """
	:param element: The element or point to hover.
	:type element: str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement` or :py:class:`Point`

	Hovers the mouse cursor over the given element or point. For example::

		hover("File size")
		hover(Button("OK"))
		hover(Link("Download"))
		hover(Point(200, 300))
		hover(ComboBox("File type").top_left + (50, 0))
	"""
        self.Mouse: MouseActions = MouseActions()
        self.write = helium.write
        """
	:param text: The text to be written.
	:type text: one of str, unicode
	:param into: The element to write into.
	:type into: one of str, unicode, :py:class:`HTMLElement`, \
:py:class:`selenium.webdriver.remote.webelement.WebElement`, :py:class:`Alert`

	Types the given text into the active window. If parameter 'into' is given,
	writes the text into the text field or element identified by that parameter.
	Common examples of 'write' are::

		write("Hello World!")
		write("user12345", into="Username:")
		write("Michael", into=Alert("Please enter your name"))
	"""

    def __str__(self) -> str:
        return "Collection of Actions from `helium` module"

    def __repr__(self) -> str:
        return self.__str__()


Element: HeliumElements = HeliumElements()
Action: HeliumActions = HeliumActions()
