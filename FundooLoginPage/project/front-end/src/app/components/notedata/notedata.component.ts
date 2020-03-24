import { Component, OnInit } from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material";
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import { AuthenticationService } from '../../services/authentication.service';
import { Message } from '@angular/compiler/src/i18n/i18n_ast';

@Component({
  selector: 'app-notedata',
  templateUrl: './notedata.component.html',
  styleUrls: ['./notedata.component.scss']
})
export class NotedataComponent implements OnInit {
 
  notes = [
    {   title: ' ',
        note: ' ',
        color: ' '}
      ]
  ParentData
  message:string;

  constructor(private userService: UserService,private dataService:DataService) {
    
   }
 
  ngOnInit() {
    
    this.getNotes();
    this.dataService.currentMessage.subscribe((message)=>{
      if(message=="Note added" || message=="Note Edited")
      this.getNotes();
    })

   
  }
  getNotes=()=>{

    this.userService.getAllNote().subscribe(
      data => {
        console.log("my data",data)
        this.notes = data;
        this.ParentData = this.notes
      },
      
      error => {
        console.log(error);
      }
    );
  }

}
