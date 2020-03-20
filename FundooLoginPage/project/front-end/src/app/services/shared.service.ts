import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';


@Injectable()
export class SharedService {

  private data = {};
  setOption(option, value) {
    this.data[option] = value;
  }

  getOption() {
    return this.data;
  }
}
