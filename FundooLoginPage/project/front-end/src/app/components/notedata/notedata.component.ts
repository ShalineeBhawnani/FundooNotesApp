import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';


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

    // this.userService.getAllNote().subscribe(
    //   data => {
    //     console.log("my data",data)
    //     this.notes = data;
    //     this.ParentData = this.notes
    //   })

    this.getNotes();
    // this.dataService.currentMessage.subscribe(message => this.message = message)
    this.dataService.currentMessage.subscribe((message)=>{
      console.log("my msg",message)
      if(message=="Note added" || message=="Note Edited")
      this.getNotes();
    })
    }
  
    
  getNotes=()=>{
    console.log("called when note added ")
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
  
  recieveMessageFromDisplay(event){
    if(event.purpose=="refresh")
    this.getNotes()
  }
  
  }