import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import {Events} from '../models/eventModel'

@Injectable({
  providedIn: 'root'
})
export class DataService {
  event:Events
  private eventCarrier=new BehaviorSubject('');
  private messageSource = new BehaviorSubject('default message');
  private labelName=new BehaviorSubject('');
  eventObservable=this.eventCarrier.asObservable();
  currentMessage = this.messageSource.asObservable();
  labelObservable=this.labelName.asObservable();
  constructor() { }
  
  sendEvent(search:string){
   this.eventCarrier.next(search);
  }

  changeMessage(message: string) {
    this.messageSource.next(message)
  }


}
