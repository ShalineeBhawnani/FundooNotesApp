import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import { SearchPipe } from '../../search.pipe';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {

  search:string
  result1:any;
  notes:any;
  searchText:any;
  message:any;
  searchNote:any;
  filterPipe: SearchPipe = new SearchPipe();
  filteredRecords:any;
  component='search';
  constructor(private dataService: DataService,private userService:UserService) { }

  ngOnInit() {
    this.dataService.eventObservable.subscribe(message => this.search = message)
   
  }

 
}
