import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: { 
    flex: 1, 
    backgroundColor: '#F8F9FE' 
  },
  // Шапка и выбор группы
  header: { 
    flexDirection: 'row', 
    justifyContent: 'space-between', 
    alignItems: 'center', 
    paddingHorizontal: 20, 
    paddingTop: 10 
  },
  title: { 
    fontSize: 24, 
    fontWeight: 'bold', 
    color: '#4834D4' 
  },
  offlineText: { 
    fontSize: 12, 
    color: '#FF9F43', 
    fontWeight: '600' 
  },
  groupSelector: { 
    flexDirection: 'row', 
    alignItems: 'center', 
    backgroundColor: '#FFF', 
    padding: 8, 
    borderRadius: 12, 
    elevation: 2, 
    shadowOpacity: 0.05 
  },
  groupText: { 
    color: '#636E72', 
    marginRight: 5, 
    fontSize: 13, 
    fontWeight: '500' 
  },
  
  // Календарная лента
  calendarContainer: { 
    paddingVertical: 15, 
    paddingLeft: 15 
  },
  dayCard: { 
    width: 55, 
    height: 75, 
    backgroundColor: '#FFF', 
    borderRadius: 18, 
    justifyContent: 'center', 
    alignItems: 'center', 
    marginRight: 12, 
    elevation: 3, 
    shadowColor: '#000', 
    shadowOpacity: 0.05, 
    shadowRadius: 10 
  },
  activeDayCard: { 
    backgroundColor: '#5E5CE6' 
  },
  dayText: { 
    fontSize: 12, 
    color: '#B2BEC3', 
    marginBottom: 4 
  },
  dateText: { 
    fontSize: 18, 
    fontWeight: 'bold', 
    color: '#2D3436' 
  },
  activeDayText: { 
    color: '#FFF' 
  },

  // Список и карточки пар
  list: { 
    padding: 20, 
    paddingBottom: 100 
  },
  lessonCard: { 
    backgroundColor: '#FFF', 
    borderRadius: 22, 
    padding: 18, 
    marginBottom: 16, 
    flexDirection: 'row', 
    elevation: 4, 
    shadowColor: '#000', 
    shadowOpacity: 0.06, 
    shadowRadius: 15 
  },
  currentLessonCard: { 
    borderLeftWidth: 5, 
    borderLeftColor: '#5E5CE6' 
  },
  timeContainer: { 
    width: 60, 
    justifyContent: 'center', 
    alignItems: 'center', 
    borderRightWidth: 1, 
    borderRightColor: '#F1F2F6', 
    paddingRight: 10 
  },
  timeStart: { 
    fontSize: 16, 
    fontWeight: 'bold', 
    color: '#2D3436' 
  },
  timeEnd: { 
    fontSize: 12, 
    color: '#B2BEC3' 
  },
  
  lessonInfo: { 
    flex: 1, 
    paddingLeft: 15 
  },
  lessonHeader: { 
    fontSize: 11, 
    color: '#A29BFE', 
    fontWeight: 'bold', 
    marginBottom: 4, 
    letterSpacing: 0.5 
  },
  subjectText: { 
    fontSize: 16, 
    fontWeight: '700', 
    color: '#2D3436', 
    marginBottom: 10 
  },
  detailsRow: { 
    flexDirection: 'row', 
    alignItems: 'center' 
  },
  detailItem: { 
    flexDirection: 'row', 
    alignItems: 'center', 
    marginRight: 18 
  },
  detailText: { 
    fontSize: 13, 
    color: '#636E72', 
    marginLeft: 5 
  },

  // Статусы
  statusBadge: { 
    position: 'absolute', 
    top: 15, 
    right: 15, 
    backgroundColor: '#FFF9E6', 
    paddingHorizontal: 10, 
    paddingVertical: 5, 
    borderRadius: 10 
  },
  statusText: { 
    fontSize: 10, 
    fontWeight: 'bold', 
    color: '#F1C40F' 
  },

  // Нижнее меню (Tab Bar)
  tabBar: { 
    position: 'absolute', 
    bottom: 25, 
    left: 20, 
    right: 20, 
    height: 75, 
    backgroundColor: '#FFF', 
    borderRadius: 30, 
    flexDirection: 'row', 
    justifyContent: 'space-around', 
    alignItems: 'center', 
    elevation: 20, 
    shadowColor: '#000', 
    shadowOpacity: 0.1, 
    shadowRadius: 20 
  },
  tabItem: { 
    alignItems: 'center', 
    justifyContent: 'center' 
  },
  tabLabel: { 
    fontSize: 11, 
    color: '#A0A0A0', 
    marginTop: 5, 
    fontWeight: '500' 
  }
});