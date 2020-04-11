import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import { MyNavComponent } from '../my-nav/my-nav.component';

@Component({
  selector: 'app-notedata',
  templateUrl: './notedata.component.html',
  styleUrls: ['./notedata.component.scss']
})
export class NotedataComponent implements OnInit {
 
  notes = [
    {   title: ' ',
        note: ' ',
     }
      ]
  ParentData
  message:string;
  searchWord: string;

  constructor(private userService: UserService,private dataService:DataService,private nav: MyNavComponent) {
    
   }
 
  ngOnInit() {

    this.nav.emitSearchEvent.subscribe((search: string) => {
      console.log("got it",this.searchWord = search);
      this.searchWord = search;
    })

    this.getNotes();
    
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
  
  }