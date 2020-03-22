import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Observable, Subject } from 'rxjs';


@Injectable()
export class SharedService {
  private subject = new Subject<any>();

  // public emitObservable: Subject<void> = new Subject<void>();

  sendMessage(message: string) {
      this.subject.next({ text: message });
  }

  getMessage(): Observable<any> {
      return this.subject.asObservable();
  }
}
