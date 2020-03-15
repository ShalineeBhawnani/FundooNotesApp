import { Component, OnInit } from '@angular/core';
import { FormGroup ,FormBuilder} from '@angular/forms';

@Component({
  selector: 'app-note',
  templateUrl: './note.component.html',
  styleUrls: ['./note.component.css']
})
export class NoteComponent implements OnInit {
  RegisterForm= FormGroup;
  loading=false;
  submitted=false;


  constructor() { }

  ngOnInit() {
  }

}
