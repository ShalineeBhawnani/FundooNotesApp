import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';

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
  // filterPipe: SearchPipe = new SearchPipe();
  filteredRecords:any;
  component='search';
  constructor(private userService: UserService,private dataService:DataService) {
  }

  ngOnInit() {
  
  }
}
