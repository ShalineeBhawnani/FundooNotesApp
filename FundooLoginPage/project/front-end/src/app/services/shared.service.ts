import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';


@Injectable()
export class SharedService {

  private usernameSource = new BehaviorSubject<string>('Onejohi Tony');
  note = this.usernameSource.asObservable()
  
  constructor() { }
  
  changeUsername(note: string) {
    this.usernameSource.next(note);
  }
}