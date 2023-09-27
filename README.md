Цель:
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

Требования:  
Создать Django проект и приложение.  
Использовать Django REST Framework для создания API.  
Реализовать модель File, которая будет представлять загруженные файлы. Модель должна содержать поля:  
file: поле типа FileField, используемое для загрузки файла.  
uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.  
processed: поле типа BooleanField, указывающее, был ли файл обработан.  
Реализовать сериализатор для модели File.  
Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели File, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.  
Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.  
Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.  

Дополнительные требования:  
Использовать Docker для развертывания проекта.  
Реализовать механизм для обработки различных типов файлов (например, изображений, текстовых файлов и т.д.).  
Предусмотреть обработку ошибок и возвращение соответствующих кодов статуса и сообщений об ошибках.  
