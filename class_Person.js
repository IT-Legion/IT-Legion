// Класс это описание характеристик
// Экземпляр это обект: Например Иванов Иван Иванович 27 лет
// Метод это действие
// Из любого класса мы можем создать столько обьектов сколько нам потребуется 
// Инкапсуляция это ?
// Сокрытие это ?
// public и  private
//https://youtu.be/-6DWwR_R4Xk?si=kPmHcQPiD_06-S7g
// Агрегация - Композиция?
// Инплимитация
// Абстрактныее классы и Интерфейсы


class Person{
    static type = "Класс Личность человека:"
    private _name;
    private _surname;
    private _yod;
    private _address;


    
    constructor(options){
        this._name  str = options.name
        this._surname str = options.surname
        this._yod int = options.year_of_birth
        this._address str = options.address
        this._height str = options.height
        this._weight str = options.weight
        
    }
    get name(){
        pass
    }
    set name(){}
    get surname(){}
    set surname(){}
    get age(){} 
    set age(){}
    get adress(){}
    set adress(){}
    voice(){}
}