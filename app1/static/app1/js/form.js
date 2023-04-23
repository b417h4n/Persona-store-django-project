function validateForm() {
    event.preventDefault();
  // Получаем значения из полей формы
  var customer_name = document.forms["delivery-form"]["customer_name"].value;
  var customer_ph_number = document.forms["delivery-form"]["customer_ph_number"].value;
  var customer_email = document.forms["delivery-form"]["customer_email"].value;
  var customer_address = document.forms["delivery-form"]["customer_address"].value;

  // Проверяем корректность введенных данных
  var phoneRegex = /^\d{11}$/;
  var emailRegex = /^\S+@\S+\.\S+$/;

  var isValid = true;
  var errorMessage = "";

  if (customer_name === "") {
    errorMessage += "Введите имя\n";
    isValid = false;
    document.getElementsByName("customer_name")[0].style.color = "red";
  }

  if (!customer_ph_number.match(phoneRegex)) {
    errorMessage += "Введите номер в формате 11 цифр\n";
    isValid = false;
    document.getElementsByName("customer_ph_number")[0].style.color = "red";

  }

  if (!customer_email.match(emailRegex)) {
    errorMessage += "Введите email в формате example@example.com\n";
    isValid = false;
    document.getElementsByName("customer_email")[0].style.color = "red";
  }

  if (customer_address === "") {
    errorMessage += "Введите адрес\n";
    isValid = false;
    document.getElementsByName("customer_address")[0].style.color = "red";
  }
  // Если введены некорректные данные, отображаем сообщения об ошибках
  if (!isValid) {
  }
  return isValid;
}
