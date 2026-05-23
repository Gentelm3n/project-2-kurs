import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  FlatList,
  ScrollView,
  Text,
  TouchableOpacity,
  View
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

// --- ИНТЕРФЕЙСЫ ---
interface Subject { id: number; name: string; short_name: string; }
interface Teacher { id: number; full_name: string; }
interface Classroom { id: number; display_name: string; }
interface TimeSlot { id: number; slot_number: number; start_time: string; end_time: string; }
interface Lesson {
  id: number;
  subject: Subject;
  teacher: Teacher;
  classroom: Classroom;
  time_slot: TimeSlot;
  lesson_type_display: string;
  day_of_week: number;
  is_active: boolean;
}

// Новый интерфейс для групп с бэкенда
interface Group {
  id: number;
  name: string;
  course: number;
  department: number;
  department_name: string;
  faculty_name: string;
}

const getWeekDays = () => {
  const startOfWeek = new Date();
  const day = startOfWeek.getDay();
  const diff = startOfWeek.getDate() - day + (day === 0 ? -6 : 1);
  const monday = new Date(startOfWeek.setDate(diff));

  return Array.from({ length: 6 }).map((_, i) => {
    const date = new Date(monday);
    date.setDate(monday.getDate() + i);
    return {
      name: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'][i],
      db_index: i + 1,
      date_number: date.getDate(),
    };
  });
};

export default function ScheduleScreen() {
  const [loading, setLoading] = useState(false);
  const [isOffline, setIsOffline] = useState(false);
  const [lessons, setLessons] = useState<Lesson[]>([]);
  
  // --- СОСТОЯНИЯ ГРУПП И ТАБОВ ---
  const [groups, setGroups] = useState<Group[]>([]); // Динамический список групп с бэкенда
  const [currentTab, setCurrentTab] = useState<'schedule' | 'profile'>('schedule');
  const [selectedGroup, setSelectedGroup] = useState('4'); // По умолчанию ID группы 9 (id=4)

  const todayIndex = new Date().getDay();
  const [selectedDay, setSelectedDay] = useState(todayIndex === 0 ? 1 : todayIndex);

  // --- ФУНКЦИЯ ЗАГРУЗКИ СПИСКА ГРУПП ---
  const loadGroups = async () => {
    try {
      const response = await axios.get('https://sfedu-app.loca.lt/api/v1/groups/', {
        headers: { 'bypass-tunnel-reminder': 'true' }
      });
      setGroups(response.data.results); // Записываем результаты в стейт
    } catch (error) {
      console.log('Ошибка при загрузке списка групп:', error);
    }
  };

  // --- ФУНКЦИЯ ЗАГРУЗКИ РАСПИСАНИЯ ---
  const loadData = async () => {
    try {
      setLoading(true);
      const response = await axios.get('https://sfedu-app.loca.lt/api/v1/schedule/', {
        params: { day_of_week: selectedDay, group: selectedGroup }, 
        headers: { 'bypass-tunnel-reminder': 'true' }
      });
      setLessons(response.data.results);
      setIsOffline(false);
    } catch (error) {
      console.log('Ошибка запроса расписания:', error);
      setIsOffline(true);
    } finally {
      setLoading(false);
    }
  };

  // Этот хук загружает список групп ВСЕГО ОДИН РАЗ при старте приложения
  useEffect(() => {
    loadGroups();
  }, []);

  // Этот хук перезапрашивает расписание при смене дня недели или выбранной группы
  useEffect(() => {
    loadData();
  }, [selectedDay, selectedGroup]); 

  const renderLesson = ({ item }: { item: Lesson }) => (
    <View style={{ padding: 15, borderBottomWidth: 1, borderColor: '#eee', opacity: item.is_active ? 1 : 0.5 }}>
      <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
        <View>
          <Text style={{ fontWeight: 'bold' }}>{item.time_slot.start_time.slice(0, 5)} - {item.time_slot.end_time.slice(0, 5)}</Text>
          <Text style={{ fontSize: 12, color: 'gray' }}>{item.time_slot.slot_number} ПАРА • {item.lesson_type_display.toUpperCase()}</Text>
        </View>
        <Text style={{ color: '#6C5CE7', fontWeight: 'bold' }}>{item.classroom.display_name}</Text>
      </View>
      <Text style={{ fontSize: 18, marginVertical: 5 }}>{item.subject.name}</Text>
      {item.teacher && (
        <View style={{ flexDirection: 'row', alignItems: 'center' }}>
          <Ionicons name="person-outline" size={14} color="gray" />
          <Text style={{ marginLeft: 5, color: 'gray' }}>{item.teacher.full_name}</Text>
        </View>
      )}
    </View>
  );

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#fff' }}>
      {/* Header */}
      <View style={{ padding: 20, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
        <View>
          <Text style={{ fontSize: 24, fontWeight: 'bold' }}>
            {currentTab === 'schedule' ? 'Расписание' : 'Профиль'}
          </Text>
          {isOffline && currentTab === 'schedule' && <Text style={{ color: 'orange' }}>Офлайн-режим (Кэш)</Text>}
        </View>
      </View>

      {currentTab === 'schedule' ? (
        <>
          {/* Calendar */}
          <View style={{ height: 90 }}>
            <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={{ paddingHorizontal: 10 }}>
              {getWeekDays().map((day, i) => (
                <TouchableOpacity
                  key={i}
                  onPress={() => setSelectedDay(day.db_index)}
                  style={{
                    width: 65, height: 75, justifyContent: 'center', alignItems: 'center', marginHorizontal: 5, borderRadius: 12,
                    backgroundColor: selectedDay === day.db_index ? '#6C5CE7' : '#f8f9fa', elevation: 2,
                  }}
                >
                  <Text style={{ fontSize: 14, color: selectedDay === day.db_index ? '#fff' : '#888' }}>{day.name}</Text>
                  <Text style={{ fontSize: 20, fontWeight: 'bold', color: selectedDay === day.db_index ? '#fff' : '#333' }}>{day.date_number}</Text>
                </TouchableOpacity>
              ))}
            </ScrollView>
          </View>

          {/* List */}
          {loading ? (
            <ActivityIndicator size="large" color="#6C5CE7" style={{ marginTop: 50 }} />
          ) : (
            <FlatList
              data={lessons}
              renderItem={renderLesson}
              keyExtractor={item => item.id.toString()}
              onRefresh={loadData}
              refreshing={loading}
              ListEmptyComponent={() => (
                <Text style={{ textAlign: 'center', marginTop: 50, color: 'gray' }}>На этот день пар не найдено</Text>
              )}
            />
          )}
        </>
      ) : (
        /* Profile View (Динамические кнопки групп) */
        <View style={{ padding: 20 }}>
          <Text style={{ fontSize: 16, color: 'gray', marginBottom: 20 }}>Выберите вашу группу:</Text>
          <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 10 }}>
            
            {/* Генерируем кнопки из стейта groups, полученного по API */}
            {groups.map((group) => (
              <TouchableOpacity
                key={group.id}
                onPress={() => {
                  setSelectedGroup(String(group.id)); // Сохраняем реальный id (число переводим в строку)
                  setCurrentTab('schedule');          // Возвращаемся к расписанию
                }}
                style={{
                  paddingVertical: 12,
                  paddingHorizontal: 20,
                  borderRadius: 10,
                  backgroundColor: selectedGroup === String(group.id) ? '#6C5CE7' : '#f0f0f0',
                  minWidth: 80,
                  alignItems: 'center'
                }}
              >
                <Text style={{ color: selectedGroup === String(group.id) ? '#fff' : '#333', fontWeight: 'bold' }}>
                  Группа {group.name}
                </Text>
              </TouchableOpacity>
            ))}

            {/* Если группы еще не успели загрузиться, показываем текст */}
            {groups.length === 0 && (
              <Text style={{ color: 'gray' }}>Загрузка списка групп...</Text>
            )}

          </View>
        </View>
      )}

      {/* Bottom Bar */}
      <View style={{ height: 60, borderTopWidth: 1, borderColor: '#eee', flexDirection: 'row', justifyContent: 'space-around', alignItems: 'center' }}>
        <TouchableOpacity 
          style={{ alignItems: 'center' }} 
          onPress={() => setCurrentTab('schedule')}
        >
          <Ionicons name="calendar" size={24} color={currentTab === 'schedule' ? "#6C5CE7" : "gray"} />
          <Text style={{ fontSize: 10, color: currentTab === 'schedule' ? "#6C5CE7" : "gray" }}>Расписание</Text>
        </TouchableOpacity>
        
        <TouchableOpacity 
          style={{ alignItems: 'center' }} 
          onPress={() => setCurrentTab('profile')}
        >
          <Ionicons name="person" size={24} color={currentTab === 'profile' ? "#6C5CE7" : "gray"} />
          <Text style={{ fontSize: 10, color: currentTab === 'profile' ? "#6C5CE7" : "gray" }}>Профиль</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}