# declarator-view
View for a table https://declarator.org/office/589

To start project run:  
`python manage.py migrate`  
`python manage.py runserver`

Meanings of the marks in a view:  
* No mark - no declaration exists
* Empty mark - there are some declarations, but there aren't any files in any of them
* Half-filled mark - there are declarations, but not all of them have files (file is None or doesn't exist)
* Filled mark - there are declarations, all with files
