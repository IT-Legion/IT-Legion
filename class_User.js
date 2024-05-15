//https://youtu.be/-6DWwR_R4Xk?si=kPmHcQPiD_06-S7g
function generateRandomId() {
    // Здесь должен быть код для генерации случайного ID
    return Math.random().toString(36).substring(2);
}

class User {
    private _username;
    private _password;
    static _id



    constructor(username, password) {
        this._username = username;
        this._password = password;
        this._id = generateRandomId();
    }

    get username() {
        return this._username;
    }
    private set username(value) {
        this._username = value;
    }

    private get password() {
        return this._password;
    }
    set password(value) {
        this._password = value;
    }

    static get id() {
        // Как правило ID статично
        return this._id;
    }
  
}

// Пример использования:
const user = new User("john_doe", "password123");
console.log(user.username); // Выведет "john_doe"
console.log(user.password); // Выведет "password123"
console.log(user.id); // Выведет случайно сгенерированный ID
