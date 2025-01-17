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
  currentMessage = this.messageSource.asObservable();
  
  eventObservable=this.eventCarrier.asObservable();
  private label=new BehaviorSubject('');
 
  labelObservable=this.label.asObservable();
 
  constructor() { }
  
  changeMessage(message: string) {
    console.log("Sharing Bet 2component",message)
    this.messageSource.next(message)
  }
  sendEvent(search:string){
    this.eventCarrier.next(search);
   }
  
  labelNext(label:string){
    this.label.next(label);
    console.log("data service label",label)
  }

}
