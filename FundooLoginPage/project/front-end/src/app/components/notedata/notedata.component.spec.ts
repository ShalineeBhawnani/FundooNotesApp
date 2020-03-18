import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NotedataComponent } from './notedata.component';

describe('NotedataComponent', () => {
  let component: NotedataComponent;
  let fixture: ComponentFixture<NotedataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NotedataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NotedataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
