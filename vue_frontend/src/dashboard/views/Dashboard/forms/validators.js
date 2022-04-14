export class Validators {
    static get required() {
      return (rowComponent) => {
        return rowComponent.value
          ? null
          : 'Required';
      };
    }
  
    static min(value) {
      return (rowComponent) => {
        return !rowComponent.value 
          ? null
          : rowComponent.value >= value
            ? null
            : `Min value: ${value}, current: ${rowComponent.value}`;
      };
    }
  
    static max(value) {
      return (rowComponent) => {
        return !rowComponent.value
          ? null
          : rowComponent.value <= value
            ? null
            : `Max value: ${value}, current: ${rowComponent.value}`;
      };
    }
  }
  